def test_login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauco")
    page.click("#login-button")

    assert "inventory" in page.url