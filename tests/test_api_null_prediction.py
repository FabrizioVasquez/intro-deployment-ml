from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app=app)

def test_null_prediction():
    response = client.post('/v1/prediction',json = {
  "opening_gross": 0,
  "screens": 2271,
  "production_budget": 13000000,
  "title_year": 1999,
  "aspect_ratio": 1.85,
  "duration": 97,
  "cast_total_facebook_likes": 0,
  "budget": 0,
  "imdb_score": 0
})
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] == 0
