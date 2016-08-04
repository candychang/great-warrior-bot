MESSAGE_TEXT = "test message"
FROM_MID ="uff2aec188e58752ee1fb0f9507c6529a"
TO_MID = "u0a556cffd4da0dd89c94fb36e36e1cdc"

MESSAGE_TYPE = 1
STICKER_TYPE = 8
MEDIA_TYPE = 2
LOCATION_TYPE = 7
CONTACT_TYPE = 10

BLOCK_TYPE = 8
ADD_FRIEND_TYPE = 4

SAMPLE_MID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
SAMPLE_NAME = "Celty Sturlson"

MESSAGE_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": "138311609000106303",
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": 1,
                    "from": FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      TO_MID
                    ],
                    "toType": 1,
                    "contentMetadata": {
                    },
                    "text": MESSAGE_TEXT,
                    "location": None
                  }
                }

STICKER_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": "138311609000106303",
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": STICKER_TYPE,
                    "from": FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      TO_MID
                    ],
                    "toType": 1,
                    "contentMetadata": {
                      "STKPKGID": "1",
                      "STKID": "1",
                      "STKVER": "100",
                      "STKTXT": "[zzz]"
                    },
                    "text": None,
                    "location": None
                  }
                }

MEDIA_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": "138311609000106303",
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": MEDIA_TYPE,
                    "from": FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      TO_MID
                    ],
                    "toType": 1,
                    "contentMetadata": {
                    },
                    "text": None,
                    "location": None
                  }
                }

LOCATION_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": "138311609000106303",
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": LOCATION_TYPE,
                    "from": FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      TO_MID
                    ],
                    "toType": 1,
                    "contentMetadata": {
                    },
                    "text": None,
                    "location": {
                      "title": "location info",
                      "address": "2-21-1 Shibuya, Shibuya-ku, Tokyo, 150-0002",
                      "latitude": 35.65910807942215,
                      "longitude": 139.70372892916203
                    }
                  }
                }

CONTACT_INFO = {
                  "id": "ABCDEF-12345678901",
                  "eventType": "138311609000106303",
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": CONTACT_TYPE,
                    "from": FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      TO_MID
                    ],
                    "toType": 1,
                    "contentMetadata": {
                      "mid": SAMPLE_MID,
                      "displayName": SAMPLE_NAME,
                    },
                    "text": None,
                    "location": None
                  }
                }

BLOCK_OPERATION = {
                      "id": "ABCDEF-12345678901",
                      "eventType": "138311609100106403",
                      "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                      "fromChannel": 1341301815,
                      "to": [
                        "u0a556cffd4da0dd89c94fb36e36e1cdc"
                      ],
                      "toChannel": 1441301333,
                      "content": {
                        "revision": 253,
                        "opType": BLOCK_TYPE,
                        "params": [
                          SAMPLE_MID,
                          None,
                          None
                        ]
                      }
                    }

ADD_FRIEND_OPERATION = {
                          "id": "ABCDEF-12345678901",
                          "eventType": "138311609100106403",
                          "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                          "fromChannel": 1341301815,
                          "to": [
                            "u0a556cffd4da0dd89c94fb36e36e1cdc"
                          ],
                          "toChannel": 1441301333,
                          "content": {
                            "revision": 253,
                            "opType": ADD_FRIEND_TYPE,
                            "params": [
                              SAMPLE_MID,
                              None,
                              None
                            ]
                          }
                        }

