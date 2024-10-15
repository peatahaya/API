from playwright.sync_api import sync_playwright

def test_response(playwright: sync_playwright):
    context = playwright.request.new_context(base_url="https://gorest.co.in")
    response = context.get(url="/public/v2/users")
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'