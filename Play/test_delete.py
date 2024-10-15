from playwright.sync_api import sync_playwright
from random_data import data, name, email


def test_response(playwright: sync_playwright):
    # Create new record
    context = playwright.request.new_context(base_url="https://gorest.co.in")
    response = context.post(url="/public/v2/users", headers={
        "Authorization": "Bearer 05594595e5cc386888b43c0457f6f97ecd5ebb6b0e108c65015fc7e45f4bdda4"
    }, data=data)
    res = response.json()
    print(response)

    assert response.status == 201
    assert res["name"] == name
    assert res["email"] == email
    print(res["id"])

    id = res["id"]

    # Delete record from db using API
    context.delete(url=f"/public/v2/users/{id}", headers={
        "Authorization": "Bearer 05594595e5cc386888b43c0457f6f97ecd5ebb6b0e108c65015fc7e45f4bdda4"
    })

    assert response.status == 201
    print(response.status)
    # Verify that record is deleted
    response = context.get(url=f"/public/v2/users/{id}", headers={
        "Authorization": "Bearer 05594595e5cc386888b43c0457f6f97ecd5ebb6b0e108c65015fc7e45f4bdda4"
    })
    assert response.status == 404
    print(response.status)
    assert response.json()["message"] == "Resource not found"
    print(response.json()["message"])