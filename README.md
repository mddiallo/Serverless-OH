# Serverless-OH

## Challenge 3 tests

curl -X POST 'http://localhost:7071/api/CreateRating' -H 'Content-Type: application/json' -d @sample.json

curl --location --request GET 'http://localhost:7071/api/GetRating?ratingId=3c2be8b7-107e-4234-a4be-61ac87579c56'

curl --location --request GET 'https://fa-bfyoc-fa-bfyoc-dev.azurewebsites.net/api/GetRating?code=sdo/vo34e3s3aaHsJZ2xGJ5TDrzGPihs8mCifWEYUUOjDCh7uag9sw==&ratingId=3a1d274f-ea6b-4c86-a088-e106f36d21ff'



curl --location --request GET 'http://localhost:7071/api/GetRatings?userId=cc20a6fb-a91f-4192-874d-132493685376'

curl --location --request GET 'https://fa-bfyoc-fa-bfyoc-dev.azurewebsites.net/api/GetRatings?code=4aXVDmtZPgb/V1qAghPJjCkElZCvgI9T2LDvhpnQIZB2/ULbHapbhw==&userId=cc5581ff-6be1-4418-a8d8-55a29c24b995'


