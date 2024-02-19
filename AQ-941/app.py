import os
from flask import Flask, Response, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = [
        {
            "companyId": 88,
            "organizationId": 725,
            "conversation": {
                "protocol": "1-3635914262963",
                "historyId": 760,
                "messageCount": 32,
                "contactId": "waent_13_5511957363353",
                "createdAt": "2021-06-07T01:52:03.782Z",
                "firstMessageAt": "2020-10-27T04:10:29.298Z",
                "lastMessageAt": "2021-06-17T19:45:10.683Z",
                "closedAt": "2022-02-26T07:47:24.634Z",
            },
            "client": {"id": 318, "name": "VplTmruGPy", "identificator": "cdJyL5LOUx"},
            "operator": {
                "assigned": {"id": 727, "name": "WfzysMQiUb", "type": 772},
                "closed": {"id": 367, "name": "lNPfBvXBXU", "type": 446},
            },
            "channel": {"id": 430, "name": "EmNPBchEtp", "identificator": "if7FqV8vIx"},
            "status": {"id": 377, "name": "ho4A2mMdJR", "type": 0},
            "sector": {"id": 215, "name": "vLEbIjbWvS", "isDefault": 1},
        },
        {
            "companyId": 67,
            "organizationId": 588,
            "conversation": {
                "protocol": "1-1400378459477",
                "historyId": 457,
                "messageCount": 15,
                "contactId": "waent_413_3389715412219",
                "createdAt": "2023-08-01T14:59:02.294Z",
                "firstMessageAt": "2021-06-13T11:11:24.999Z",
                "lastMessageAt": "2022-10-02T10:57:06.154Z",
                "closedAt": "2022-08-25T12:29:48.207Z",
            },
            "client": {"id": 190, "name": "Fw1pW8I2F5", "identificator": "HcFOVlfhH5"},
            "operator": {
                "assigned": {"id": 392, "name": "GmY1XpUEG9", "type": 20},
                "closed": {"id": 689, "name": "XLZkwgW5mN", "type": 532},
            },
            "channel": {"id": 681, "name": "BOgNZDsvHx", "identificator": "OSiNvpAsLb"},
            "status": {"id": 482, "name": "cYjGpM3Z6V", "type": 0},
            "sector": {"id": 287, "name": "vxMFe6HZl4", "isDefault": 1},
        },
        {
            "companyId": 38,
            "organizationId": 672,
            "conversation": {
                "protocol": "8-7739764688561",
                "historyId": 263,
                "messageCount": 11,
                "contactId": "waent_572_2942251322130",
                "createdAt": "2022-07-07T08:55:31.033Z",
                "firstMessageAt": "2021-02-16T23:26:47.061Z",
                "lastMessageAt": "2021-04-26T14:56:36.594Z",
                "closedAt": "2021-03-17T15:18:47.934Z",
            },
            "client": {"id": 644, "name": "GWbYGR4Lr8", "identificator": "VIQJy5nZ5K"},
            "operator": {
                "assigned": {"id": 904, "name": "FE7mGv4NKS", "type": 99},
                "closed": {"id": 303, "name": "JkEerMCnjI", "type": 13},
            },
            "channel": {"id": 565, "name": "BePm3WFkg1", "identificator": "K7WQrBqBQY"},
            "status": {"id": 453, "name": "p65Tqy1WbW", "type": 0},
            "sector": {"id": 919, "name": "QyxeoQlf6r", "isDefault": 1},
        },
        {
            "companyId": 93,
            "organizationId": 707,
            "conversation": {
                "protocol": "7-8616834137475",
                "historyId": 832,
                "messageCount": 47,
                "contactId": "waent_902_5782169936195",
                "createdAt": "2021-06-02T02:48:09.196Z",
                "firstMessageAt": "2020-12-17T21:06:31.122Z",
                "lastMessageAt": "2021-12-06T04:43:06.154Z",
                "closedAt": "2021-07-02T05:43:37.289Z",
            },
            "client": {"id": 584, "name": "P23b5qRyjI", "identificator": "JfPQZ7sCyD"},
            "operator": {
                "assigned": {"id": 480, "name": "T6P0QQUrxB", "type": 500},
                "closed": {"id": 607, "name": "Z3VFZpQ2W0", "type": 48},
            },
            "channel": {"id": 860, "name": "OQnEkSKw5q", "identificator": "iFZxgMdLxl"},
            "status": {"id": 430, "name": "LHDCYkbwUe", "type": 0},
            "sector": {"id": 357, "name": "UvdumBJtYJ", "isDefault": 1},
        },
        {
            "companyId": 17,
            "organizationId": 839,
            "conversation": {
                "protocol": "9-2568020196149",
                "historyId": 973,
                "messageCount": 28,
                "contactId": "waent_477_5718780185951",
                "createdAt": "2022-03-27T14:32:11.334Z",
                "firstMessageAt": "2021-10-01T04:45:29.574Z",
                "lastMessageAt": "2022-04-06T10:17:48.229Z",
                "closedAt": "2021-11-16T10:56:22.131Z",
            },
            "client": {"id": 405, "name": "hw3GgCql49", "identificator": "i9aAexs1Qi"},
            "operator": {
                "assigned": {"id": 641, "name": "evRxOfO4oa", "type": 522},
                "closed": {"id": 584, "name": "hOAVhv3u50", "type": 196},
            },
            "channel": {"id": 900, "name": "yYUfN3v3Iy", "identificator": "MJ5FXnQ0Ft"},
            "status": {"id": 200, "name": "GwlxSd7VGs", "type": 0},
            "sector": {"id": 936, "name": "YLv5FcVRMs", "isDefault": 1},
        },
        {
            "companyId": 60,
            "organizationId": 700,
            "conversation": {
                "protocol": "3-3336912664924",
                "historyId": 305,
                "messageCount": 5,
                "contactId": "waent_151_3183491580745",
                "createdAt": "2021-05-03T00:32:45.290Z",
                "firstMessageAt": "2021-05-14T12:44:14.671Z",
                "lastMessageAt": "2022-01-29T10:00:06.357Z",
                "closedAt": "2022-01-23T23:02:31.999Z",
            },
            "client": {"id": 369, "name": "x6TzHbg5Ky", "identificator": "dF4Bpn8N7A"},
            "operator": {
                "assigned": {"id": 256, "name": "u1N5wHZ28H", "type": 655},
                "closed": {"id": 263, "name": "NOg5CwExF1", "type": 663},
            },
            "channel": {"id": 395, "name": "nEZJLRX2Ry", "identificator": "cQ4uep6SHj"},
            "status": {"id": 129, "name": "wHY5g5wxfo", "type": 0},
            "sector": {"id": 814, "name": "2A5jmYVCrG", "isDefault": 1},
        },
        {
            "companyId": 83,
            "organizationId": 246,
            "conversation": {
                "protocol": "8-6931375033289",
                "historyId": 118,
                "messageCount": 14,
                "contactId": "waent_479_4667124763307",
                "createdAt": "2022-03-30T19:32:29.103Z",
                "firstMessageAt": "2022-02-22T08:25:15.873Z",
                "lastMessageAt": "2022-04-10T09:43:40.986Z",
                "closedAt": "2021-08-08T19:11:50.384Z",
            },
            "client": {"id": 855, "name": "MbmmdYrSHg", "identificator": "QVrgU8x4Hi"},
            "operator": {
                "assigned": {"id": 865, "name": "4qy0V01vVc", "type": 59},
                "closed": {"id": 243, "name": "1rVdgntIyS", "type": 503},
            },
            "channel": {"id": 842, "name": "1gFstsj9Uw", "identificator": "esZ8tvP5Ie"},
            "status": {"id": 654, "name": "nF6uFqWiRx", "type": 0},
            "sector": {"id": 134, "name": "9rgvp1AfWs", "isDefault": 1},
        },
        {
            "companyId": 50,
            "organizationId": 430,
            "conversation": {
                "protocol": "9-5093863132095",
                "historyId": 202,
                "messageCount": 44,
                "contactId": "waent_197_2116881146257",
                "createdAt": "2023-03-03T16:44:56.646Z",
                "firstMessageAt": "2022-05-25T21:51:00.815Z",
                "lastMessageAt": "2022-08-07T23:18:33.022Z",
                "closedAt": "2021-06-23T17:05:08.350Z",
            },
            "client": {"id": 465, "name": "5jGBZjH1aG", "identificator": "zcd4avHyTn"},
            "operator": {
                "assigned": {"id": 669, "name": "F9ZfRmGeO3", "type": 394},
                "closed": {"id": 201, "name": "3twbHBK1YJ", "type": 989},
            },
            "channel": {"id": 528, "name": "GnL3YJpr57", "identificator": "uz02KFA8I2"},
            "status": {"id": 145, "name": "8OJGH0S8JD", "type": 0},
            "sector": {"id": 345, "name": "Z0wF9qmcO3", "isDefault": 1},
        },
        {
            "companyId": 96,
            "organizationId": 883,
            "conversation": {
                "protocol": "6-6782281339667",
                "historyId": 419,
                "messageCount": 16,
                "contactId": "waent_479_4169497072372",
                "createdAt": "2021-05-21T10:00:00.114Z",
                "firstMessageAt": "2021-05-25T13:50:46.392Z",
                "lastMessageAt": "2021-07-15T14:26:43.400Z",
                "closedAt": "2021-11-25T04:26:24.233Z",
            },
            "client": {"id": 573, "name": "h6Ky3arFqW", "identificator": "67Rb8zKmF3"},
            "operator": {
                "assigned": {"id": 180, "name": "d3Le3z0eCu", "type": 404},
                "closed": {"id": 369, "name": "bSg3F7CjLv", "type": 1},
            },
            "channel": {"id": 266, "name": "lI3C1Ve1bo", "identificator": "lfiEs9enjD"},
            "status": {"id": 250, "name": "L8SRfCYwQ5", "type": 0},
            "sector": {"id": 286, "name": "5v0y9CXyRm", "isDefault": 1},
        },
        {
            "companyId": 94,
            "organizationId": 984,
            "conversation": {
                "protocol": "7-6438221352987",
                "historyId": 354,
                "messageCount": 31,
                "contactId": "waent_541_1342299422271",
                "createdAt": "2022-01-29T15:06:05.158Z",
                "firstMessageAt": "2021-11-12T02:47:59.300Z",
                "lastMessageAt": "2022-03-02T05:29:08.707Z",
                "closedAt": "2021-11-19T22:26:49.940Z",
            },
            "client": {"id": 954, "name": "7Xsucr0vQ1", "identificator": "iL5Pamzz3P"},
            "operator": {
                "assigned": {"id": 154, "name": "wtDSf6f9w9", "type": 314},
                "closed": {"id": 581, "name": "bDWy9aK7vC", "type": 411},
            },
            "channel": {"id": 276, "name": "aHgtCbc0u0", "identificator": "5wT9Ae2rXl"},
            "status": {"id": 793, "name": "p8z7eQD5jD", "type": 0},
            "sector": {"id": 511, "name": "Qcft1hXGMl", "isDefault": 1},
        },
        {
            "companyId": 43,
            "organizationId": 684,
            "conversation": {
                "protocol": "4-8582189252682",
                "historyId": 845,
                "messageCount": 13,
                "contactId": "waent_755_9790002540246",
                "createdAt": "2022-01-05T05:53:12.861Z",
                "firstMessageAt": "2021-07-14T09:53:31.893Z",
                "lastMessageAt": "2022-02-26T12:54:13.026Z",
                "closedAt": "2021-07-27T16:18:01.863Z",
            },
            "client": {"id": 134, "name": "Hg0j7tOTfC", "identificator": "t2GEbZ2gPa"},
            "operator": {
                "assigned": {"id": 713, "name": "NsiQt3jvS6", "type": 918},
                "closed": {"id": 366, "name": "TkkbOwHUj8", "type": 614},
            },
            "channel": {"id": 728, "name": "30vvu0j8u0", "identificator": "yU63a8fPp7"},
            "status": {"id": 665, "name": "bkM2gyRLZl", "type": 0},
            "sector": {"id": 693, "name": "9VOsI7kM3t", "isDefault": 1},
        },
    ]
    return jsonify(data)

    return Response("ok")


if __name__ == "__main__":
    # Use the environment variable 'PORT' if set, otherwise use 5001 as the default
    port = int(os.environ.get("PORT", 5005))
    app.run(debug=False, port=port, host="0.0.0.0")
