MESSAGE_EVENT = "138311609000106303"
OPERATION_EVENT = "138311609100106403"

TEXT = 1
STICKER = 8
IMAGE = 2
VIDEO = 3
AUDIO = 4
LOCATION = 7
CONTACT = 10

BLOCK = 8
ADD_FRIEND = 4


SAMPLE_MESSAGE_TEXT = "test message"
SAMPLE_FROM_MID ="uff2aec188e58752ee1fb0f9507c6529a"
SAMPLE_TO_MID = "u0a556cffd4da0dd89c94fb36e36e1cdc"

SAMPLE_MID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
SAMPLE_NAME = "Celty Sturlson"

TEXT_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": MESSAGE_EVENT,
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    SAMPLE_TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": TEXT,
                    "from": SAMPLE_FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      SAMPLE_TO_MID
                    ],
                    "toType": 1,
                    "contentMetadata": {
                    },
                    "text": SAMPLE_MESSAGE_TEXT,
                    "location": None
                  }
                }

STICKER_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": MESSAGE_EVENT,
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    SAMPLE_TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": STICKER,
                    "from": SAMPLE_FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      SAMPLE_TO_MID
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

IMAGE_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": MESSAGE_EVENT,
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    SAMPLE_TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": IMAGE,
                    "from": SAMPLE_FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      SAMPLE_TO_MID
                    ],
                    "toType": 1,
                    "contentMetadata": {
                    },
                    "text": None,
                    "location": None
                  }
                }

VIDEO_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": MESSAGE_EVENT,
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    SAMPLE_TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": VIDEO,
                    "from": SAMPLE_FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      SAMPLE_TO_MID
                    ],
                    "toType": 1,
                    "contentMetadata": {
                    },
                    "text": None,
                    "location": None
                  }
                }

AUDIO_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": MESSAGE_EVENT,
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    SAMPLE_TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": AUDIO,
                    "from": SAMPLE_FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      SAMPLE_TO_MID
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
                  "eventType": MESSAGE_EVENT,
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    SAMPLE_TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": LOCATION,
                    "from": SAMPLE_FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      SAMPLE_TO_MID
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

CONTACT_EVENT = {
                  "id": "ABCDEF-12345678901",
                  "eventType": MESSAGE_EVENT,
                  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                  "fromChannel": 1341301815,
                  "to": [
                    SAMPLE_TO_MID
                  ],
                  "toChannel": 1441301333,
                  "content": {
                    "id": "325708",
                    "contentType": CONTACT,
                    "from": SAMPLE_FROM_MID,
                    "createdTime": 1462629479859,
                    "to": [
                      SAMPLE_TO_MID
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
                      "eventType": OPERATION_EVENT,
                      "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                      "fromChannel": 1341301815,
                      "to": [
                        "u0a556cffd4da0dd89c94fb36e36e1cdc"
                      ],
                      "toChannel": 1441301333,
                      "content": {
                        "revision": 253,
                        "opType": BLOCK,
                        "params": [
                          SAMPLE_MID,
                          None,
                          None
                        ]
                      }
                    }

ADD_FRIEND_OPERATION = {
                          "id": "ABCDEF-12345678901",
                          "eventType": OPERATION_EVENT,
                          "from": "u206d25c2ea6bd87c17655609a1c37cb8",
                          "fromChannel": 1341301815,
                          "to": [
                            "u0a556cffd4da0dd89c94fb36e36e1cdc"
                          ],
                          "toChannel": 1441301333,
                          "content": {
                            "revision": 253,
                            "opType": ADD_FRIEND,
                            "params": [
                              SAMPLE_MID,
                              None,
                              None
                            ]
                          }
                        }

