# demo-apihandler


Web Server API endpoint to expose
  * build model server
    - input :
      - model location
      - model input specification
    - returns
      - success code

  * deploy model server
    - input :
      - host to deploy to
      - location of model to deploy
      - version
    - returns
        - success code

  * update model
    - input :
      - host to deploy to
      - location of model
      - flag [to use updated model?]

  * predict
    - input :
       - model name?
       - input to model ( as json )
    - returns :
       success code
       prediction
