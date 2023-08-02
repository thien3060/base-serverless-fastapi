# base-serverless-fastapi

# start project local:
- `npm install`
- `serverless dynamodb install`
- `serverless dynamodb start`
- `serverless offline`

# serverless commands:
- config/init dev stage `serverless`
- deploy `serverless deploy`
- deploy other stage `serverless deploy --stage production --region ap-southeast-1`
- deploy a function (fast deploy) `serverless deploy function --function app serverless-fastapi-dev-app`
- run offline mode `serverless offline`

# local dynamodb setup
- `serverless dynamodb install`
- `serverless dynamodb migrate`
- `serverless dynamodb start`

# update environment
- `pip install package && pip freeze > requirements.txt`