# Smart Factory product quality classification 
URL : <https://dacon.io/competitions/official/236055/overview/description>  
Public : #74
Private : #143
### Experiments
* Data Features
  * Product ID
  * Timestamp 
  * Line : Types of Line where the products are produced
  * Product Code : Types of Prodcut
  * X1 ~ X2875 : Classified value for manufacturing  
* Feature Engineering
  *  Split the data which has same Line type 
    *  In manufacuring, products are produce in lines. I thought classified values are related at Line type.
  *  Change missing values to 0
    *  evaluate the performace for RandomForest model that which missing value strategy performs best.
  * Add \'Y_Quality\' features for training
    *  This change makes performance better than data without \'Y_Quality\'
  
* Model
  *  LightGBM
  *  XGBoost
  *  RandomForest
  *  AutoGluon
