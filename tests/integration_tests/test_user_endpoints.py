def test_delete_user_success(testing_app, valid_user_delete_id):
    response = testing_app.delete(f"/user/{valid_user_delete_id}")
    assert response.status_code == 200


