def test_get_activities_returns_dictionary(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0


def test_each_activity_has_expected_fields(client):
    # Arrange
    endpoint = "/activities"
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)
    activities_data = response.json()

    # Assert
    assert response.status_code == 200
    for activity in activities_data.values():
        assert expected_fields.issubset(activity.keys())
        assert isinstance(activity["participants"], list)
