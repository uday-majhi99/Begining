# alarm_clock.py
# Run: python alarm_clock.py
# Features: multiple alarms, daily repeat, labels, snooze, list/remove

import sys
import time
import datetime as dt
import threading
from typing import List, Optional

try:
    import winsound  # Windows beep
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False


def beep(times: int = 3, interval: float = 0.6):
    """Cross-platform audible alert."""
    for _ in range(times):
        if HAS_WINSOUND and sys.platform.startswith("win"):
            # Frequency 1000 Hz, duration 300 ms
            winsound.Beep(1000, 300)
        else:
            # ASCII bell (may or may not make sound depending on terminal)
            sys.stdout.write("\a")
            sys.stdout.flush()
        time.sleep(interval)


class Alarm:
    def __init__(self, hour: int, minute: int, label: str = "", repeat_daily: bool = False):
        self.hour = hour
        self.minute = minute
        self.label = label.strip()
        self.repeat_daily = repeat_daily
        self.next_trigger = self._compute_next_trigger()

    def _compute_next_trigger(self) -> dt.datetime:
        now = dt.datetime.now()
        today_trigger = now.replace(hour=self.hour, minute=self.minute, second=0, microsecond=0)
        if today_trigger <= now:
            # schedule for tomorrow
            today_trigger += dt.timedelta(days=1)
        return today_trigger

    def reschedule_after_snooze(self, minutes: int):
        self.next_trigger = dt.datetime.now() + dt.timedelta(minutes=minutes)

    def reschedule_next_day(self):
        self.next_trigger = self.next_trigger + dt.timedelta(days=1)

    @property
    def time_str(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

    def __repr__(self):
        flags = []
        if self.repeat_daily:
            flags.append("daily")
        if self.label:
            flags.append(f"label='{self.label}'")
        flags_str = f" ({', '.join(flags)})" if flags else ""
        return f"{self.time_str}{flags_str} → next: {self.next_trigger.strftime('%Y-%m-%d %H:%M:%S')}"


class AlarmManager:
    def __init__(self):
        self._alarms: List[Alarm] = []
        self._stop_event = threading.Event()
        self._lock = threading.Lock()

    def add_alarm(self, alarm: Alarm):
        with self._lock:
            self._alarms.append(alarm)

    def list_alarms(self) -> List[Alarm]:
        with self._lock:
            return sorted(self._alarms, key=lambda a: a.next_trigger)

    def remove_alarm(self, index: int) -> bool:
        with self._lock:
            if 0 <= index < len(self._alarms):
                self._alarms.pop(index)
                return True
            return False

    def next_alarm(self) -> Optional[Alarm]:
        with self._lock:
            if not self._alarms:
                return None
            return min(self._alarms, key=lambda a: a.next_trigger)

    def stop(self):
        self._stop_event.set()

    def run(self):
        """Main loop: waits for next alarm, triggers and handles snooze/dismiss."""
        try:
            while not self._stop_event.is_set():
                nxt = self.next_alarm()
                if not nxt:
                    # No alarms; sleep briefly and continue
                    time.sleep(0.5)
                    continue

                now = dt.datetime.now()
                wait_secs = (nxt.next_trigger - now).total_seconds()
                if wait_secs > 0:
                    # Sleep in small chunks so Ctrl+C is responsive
                    sleep_chunk = min(wait_secs, 1.0)
                    time.sleep(sleep_chunk)
                    continue

                # Trigger alarm
                print("\n" + "=" * 60)
                print(f"⏰ ALARM!  {nxt.time_str}  {f'— {nxt.label}' if nxt.label else ''}")
                print("=" * 60)
                beep(4, 0.5)

                # Ask user what to do
                while True:
                    try:
                        choice = input("Choose action: [S]nooze (min), [D]ismiss, [R]emove: ").strip().lower()
                    except (EOFError, KeyboardInterrupt):
                        choice = "d"

                    if choice == "s" or choice.startswith("s"):
                        try:
                            mins = int(input("Snooze minutes (e.g., 5): ").strip())
                            if mins <= 0:
                                print("Enter a positive number.")
                                continue
                        except ValueError:
                            print("Invalid number.")
                            continue
                        nxt.reschedule_after_snooze(mins)
                        print(f"Snoozed for {mins} minute(s). Next at {nxt.next_trigger.strftime('%H:%M:%S')}.")
                        break

                    elif choice == "d" or choice.startswith("d"):
                        if nxt.repeat_daily:
                            # schedule same time next day
                            nxt.reschedule_next_day()
                            print(f"Dismissed. Repeats daily → {nxt.next_trigger.strftime('%Y-%m-%d %H:%M:%S')}")
                        else:
                            # one-shot: remove it
                            with self._lock:
                                try:
                                    self._alarms.remove(nxt)
                                    print("Dismissed. (One-time alarm removed.)")
                                except ValueError:
                                    pass
                        break

                    elif choice == "r" or choice.startswith("r"):
                        with self._lock:
                            try:
                                self._alarms.remove(nxt)
                                print("Alarm removed.")
                            except ValueError:
                                pass
                        break

                    else:
                        print("Please choose S, D, or R.")
        except KeyboardInterrupt:
            print("\nStopping alarm manager…")
        finally:
            self._stop_event.set()


def parse_time(hhmm: str) -> Optional[tuple]:
    try:
        parts = hhmm.strip().split(":")
        if len(parts) != 2:
            return None
        h = int(parts[0])
        m = int(parts[1])
        if not (0 <= h <= 23 and 0 <= m <= 59):
            return None
        return h, m
    except Exception:
        return None


def main_menu():
    mgr = AlarmManager()

    def print_menu():
        print("\n" + "-" * 60)
        print("Alarm Clock")
        print("-" * 60)
        print("1) Add alarm")
        print("2) List alarms")
        print("3) Remove alarm")
        print("4) Start alarm loop")
        print("5) Exit")

    while True:
        print_menu()
        choice = input("Select option [1-5]: ").strip()

        if choice == "1":
            hhmm = input("Enter time (24h HH:MM): ").strip()
            parsed = parse_time(hhmm)
            if not parsed:
                print("Invalid time format.")
                continue
            label = input("Optional label: ").strip()
            rep = input("Repeat daily? [y/N]: ").strip().lower().startswith("y")
            alarm = Alarm(parsed[0], parsed[1], label=label, repeat_daily=rep)
            mgr.add_alarm(alarm)
            print(f"Added alarm: {alarm}")

        elif choice == "2":
            alarms = mgr.list_alarms()
            if not alarms:
                print("No alarms.")
            else:
                for i, a in enumerate(alarms):
                    print(f"{i}) {a}")

        elif choice == "3":
            alarms = mgr.list_alarms()
            if not alarms:
                print("No alarms to remove.")
                continue
            for i, a in enumerate(alarms):
                print(f"{i}) {a}")
            try:
                idx = int(input("Index to remove: ").strip())
            except ValueError:
                print("Invalid index.")
                continue
            # Map displayed index back to original list index
            # since list_alarms() returns sorted copy, we need to find the exact object
            if 0 <= idx < len(alarms):
                target = alarms[idx]
                # remove matching object from manager
                removed = False
                for j, original in enumerate(mgr._alarms):
                    if original is target:
                        mgr.remove_alarm(j)
                        removed = True
                        break
                print("Removed." if removed else "Failed to remove.")
            else:
                print("Index out of range.")

        elif choice == "4":
            print("Starting alarm loop. Press Ctrl+C to stop.")
            mgr.run()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please choose a valid option (1-5).")


if __name__ == "__main__":
    main_menu()
