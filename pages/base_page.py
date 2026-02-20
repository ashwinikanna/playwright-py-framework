from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

# ---------- Navigation ----------
    def goto(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")


    # ---------- Locators ----------
    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    # ---------- Actions (stable wrappers) ----------
    def click(self, selector: str) -> None:
        loc = self.locator(selector)
        expect(loc).to_be_visible(timeout=10000)
        expect(loc).to_be_enabled()
        loc.click()
    
    def click_by_role(self, role: str, name: str) -> None:
        loc = self.page.get_by_role(role, name=name)
        expect(loc).to_be_visible()
        expect(loc).to_be_enabled()
        loc.click()

    def fill(self, selector: str, value: str, clear_first: bool = True) -> None:
        loc = self.locator(selector)
        expect(loc).to_be_visible()
        if clear_first:
            loc.fill("")  # ensures clean input
        loc.fill(value)

    def type(self, selector: str, value: str) -> None:
        loc = self.locator(selector)
        expect(loc).to_be_visible()
        loc.type(value)

    def submit(self):
     self.page.get_by_role("button", name="Login").click()

# ---------- Assertions (generic, reusable) ----------
    def expect_visible(self, selector: str) -> None:
        expect(self.locator(selector)).to_be_visible()

    def expect_hidden(self, selector: str) -> None:
        expect(self.locator(selector)).to_be_hidden()

    def expect_text_contains(self, selector: str, text: str) -> None:
        expect(self.locator(selector)).to_contain_text(text)

    def expect_url_contains(self, partial: str) -> None:
        expect(self.page).to_have_url(lambda url: partial in url)

    # ---------- Waiting helpers ----------
    def wait_for_selector(self, selector: str) -> None:
        self.page.wait_for_selector(selector, state="visible")

    def wait_for_network_idle(self) -> None:
        self.page.wait_for_load_state("networkidle")