# How to use the Spotify WEB API 
> Only for getting user's past 50 songs listened to

Note that the code you obtain from these steps is only valid for 10 min! This is a preliminary script but I will try to automate it in the future!

1. In this folder, run `npm install`
2. Run `node spotify_auth.js`. This returns a URL that you can paste into the browser. The page, after authorising the API to access user data, should redirect to google. The URL, however will look something like this:
`https://www.google.com/?code=AQBSt01BikJIZShOkYj0TzZkCCn4u6cXFsqNGJIAchKkJmxvjoo2ObYNdksmXS0fSPVk1fW5t26DZ5MBFKvn26O2Md9RlaURGlaan5S_C_nns60pxfdvhg7hkWuCUFAiMv9DuVBhLbOx41s8VWc3wSl0oG7nG3E-r9dNPhUsrlSpLWa3UxIT2EVvvhess9iGTFlptLbfBtjBaa76sv9eaus2g-IVuh6MvCnFrAX3Tow2Lpe3Zmk6SEh_C3eSuIPjnZfoT3yJrO8Ur1wjo65C_AyfL_ZXnV9X56kU2KbUF0E3QN4`
3. Grab the string after `code=` and copy it into the `return_code` variable in spotify_auth.js
4. Run `node spotify_auth.js` again and copy and run the full curl command in terminal
5. This should return a JSON object with a token. Copy this token into the `token` variable in spotify_api.js
6. Run `node spotify_api.js` and the return value will be the names of the top 50 songs that you would have listened to.
