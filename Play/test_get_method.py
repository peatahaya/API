from playwright.sync_api import sync_playwright

def test_get(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get(url="https://gorest.co.in/public/v2/users/7471651")
    print(response)
