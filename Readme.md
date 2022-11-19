# Facebook Graph API 
###### Instagram's Post Insights

## Description

The Project is about fetching Instagram posts insights of creators/businesses using Facebook Graph API. The code is written python language. Flask framework is used for publishing data in web to visualize posts insights. For frontend, basic html and CSS is used.

## Process to generate "Access Token" for having access to Facebook Graph API:

1. Create an FB business Page
2. Instagram account should be professional account(creator or business) as facebook doesn't shares personal account insights. 
3. Link the Instagram account with FB business page.
4. Go to Meta for developer website and  make developer account in Meta.
5. Go to My Apps > Click on Create App 
6. Select App type as business and give name to app in details section.
7. Once your App is ready, In Add Product Section > Add Instagram Graph API.
8. Go to tools section 
9. Click on Generate access token, the token is important for API request.
10. Click on Add Permission and add following permission to have access to posts insights: instagram_basic, instagram_manage_insights, pages_show_list, pages_read_engagement, and pages_read_user_content.
11. After adding permissions, while generating access token facebook will ask to link instagram business account and fb business page. During this process please copy and store the Instagram account it will be required in code
12. If you have converted your personal account to professional then you will get insights on those posts only which are posted after conversion.


## Run the code 
 1. Flask should be installed in system.
 2. In FBData_API.py, add access token, ig username and instagram account id.
 3. Run the Main.py file
 4. Don't delete or move the template folder as it contains html files.

 You can check the how final output will look like in Webapp_SS.png image.

Thank you :)

Learner,
Chaitanya 

