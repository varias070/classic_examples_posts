def test_author_resource(client):
    create_author_result = client.simulate_post(
        "/author",
        json={
            "name": "Auto Test Author",
            "phone": "7999887766",
        },
    )
    assert create_author_result.status_code == 200

    author_id = create_author_result.json
    result = client.simulate_get(
        "/author",
        params={"id": author_id},
    )

    assert result.status_code == 200
    assert result.json == {
        "id": author_id,
        "name": "Auto Test Author",
        "phone": "7999887766",
    }
