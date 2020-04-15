'use strict';
let log = console.log

let request = require("request");
var scopes = 'user-read-private user-read-email user-read-recently-played';
let user_uri = "1151298265"
var token = "BQCoYeJyXczJv-OnYJbW90_Q4jgYK2esdLjzy5MTg1Iu9-HnOfc3CvNeWyJPaV-5SR0ch-f4xujDJgCOknDT3krBrV-Z_HJu9sHVF4RvmCcT8Vv4ykF0Ioe6HbxBh3OiODSj3Y9BdGLQWE9H8U4HoMPNojhTTDfZgcLUkWIgKs2O1uw";
var recently_played_url = "https://api.spotify.com/v1/me/player/recently-played?limit=50"

request({url: recently_played_url, headers:{"Authorization": "Bearer " + token}}, (err, res) => {
    if (res) {
        let songs_list = JSON.parse(res.body).items
        songs_list.forEach(song => {
            log(song.track.name)
        });
    }
})