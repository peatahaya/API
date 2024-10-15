from playwright.sync_api import sync_playwright

def test_response(playwright: sync_playwright):
    context = playwright.request.new_context(base_url="https://gorest.co.in")
    response = context.get(url="/public/v2/users")
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'
    res = response.json()
    print(res[0].get("name"))
    assert res[0].get("name") == "Miss Kamala Kapoor"

    size = len(res)
    print(size)

    for i in range(0, size+1):
        print(res[i].get("name"))
        if res[i].get("name") == "Darshwana Abbott Ret.":
            assert res[i].get("name") == "Darshwana Abbott Ret."
            break