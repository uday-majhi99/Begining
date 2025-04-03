from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Open browser
        page = browser.new_page()

        # Redirect directly to Google
        page.goto("https://www.google.com")

        browser.close()


if __name__ == "__main__":
    main()