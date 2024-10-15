from playwright.sync_api import sync_playwright

def test_get(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get(url="https://gorest.co.in/public/v2/users/7471651")
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'
    print(response.json()["name"])
    print(response.json()["email"])
    print(response.json()["gender"])
    print(response.json()["status"])
    res = response.json()
    # First method of asserting a name
    assert response.json()["name"] == "Digambar Talwar Jr."
    # Second method of asserting a name
    assert res.get("name") == "Digambar Talwar Jr."
    assert response.headers["content-type"] == "application/json; charset=utf-8"