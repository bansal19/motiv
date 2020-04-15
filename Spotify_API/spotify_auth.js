'use strict';

let request = require("request");
let log = console.log

// Request authorisation from spotify web servers
let client_id = "d82fe2d290ff4db6a10afd084053ffa9";
let redirect_uri = encodeURIComponent("https://www.google.com/");
let scope = "user-read-private%20user-read-email%20playlist-read-private%20user-read-recently-played"

let auth_url = "https://accounts.spotify.com/authorize?client_id=" + client_id + "&response_type=code&redirect_uri=" + redirect_uri + "&scope=" + scope;
log("----------- Paste the below url in your browser --------------")
log(auth_url)

let return_code = "AQCNdEmjsSjXKCkiNOspN4UpxfHNtxjTq633aPISPvlxI2Yzrb4Cu6G9PgnXAUtoZ-SGKOiYKXvwf6OH86boUFN1lupAx6aboJ9z1uXS8WL-pJ57TYeZ3NORTuXmebX5U6i84sg2J4SdOMXS4H5h9QDybAyXIJXjKLNJfnLWPNAV3Mm9DOchEtyF_4lgsrMjZFujSJSXfoLhTErLAzXAhQpYPIni3voS7WyB1bqv5T3MlZ1ztpmFYVG3bwXGArkZL5-AteMyuNhuu25K9fdVk3ZVv1d9q8gcPsyha93To7XnZ_s"
let client_id_client_secret_base_64 = "ZDgyZmUyZDI5MGZmNGRiNmExMGFmZDA4NDA1M2ZmYTk6NDg4OTdmMDRhMzQ5NGE5NWE3YmQ2NWMxOWJlNjM4OTA="

log("----------- cURL Request --------------")

let curl_request = "curl -H \"Authorization: Basic " + client_id_client_secret_base_64 + "\" -d grant_type=authorization_code -d code=" + return_code + " -d redirect_uri=https%3A%2F%2Fwww.google.com%2F https://accounts.spotify.com/api/token"

log(curl_request)
// Return value of above cURL command should look like this after running in terminal:
//{"access_token":"BQB3_ZHtVxmjeHi5ynMshLo2RbH3uX1VT5SXoDWYH5E0tm0xkNVYDr4haziyGno3GyWLvAxVk0NGjvXsa37RZ3F6djWaCXr8YgQAfwWOqKs2kn0bW1Wa2HzLJc0ZHnktJW5OF8CdAmP3qokuRwtIq7lLtTG689e2iJPElLbdwL2A","token_type":"Bearer","expires_in":3600,"refresh_token":"AQBF6wzuvf1477VI8MlVdGqDqw87P9O8P4eI1_Psurr0FNqyv-d6Fy7bB9BrBRp240OE6fIO-k7PLN0apUMax7Ma0RzUu1IkC2HFfsIxo95dq_g25rKRe_qYrAZDeaKE5Rs","scope":"playlist-read-private user-read-email user-read-private"}