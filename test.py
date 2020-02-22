class templateModelResponse:

    def test(self, a):
          return {
          "string": a["string"],
          "object_id": a["object_id"]
      }

    def modelAdapter(self, it):
        return list(map(self.test, it))

    def test2(self, item):
        arr = self.modelAdapter(item)
        return {
            "data": arr
        }
    
    # def __init__(self, item):
    #     # self.name = "FUCK"
    #     # self.surname = "YOU"
    #     self.object_id = str(item["object_id"])
    #     self.string = str(item["string"])

# def templateModelResponse(a):
#       return {
#           "string": a["string"],
#           "object_id": a["object_id"]
#       }

x = {
      "_id": {
        "$oid": "5e4f7c0b6cce7bc7531f8a5e"
      },
      "object_id": "1",
      "string": "test",
      "date": {
        "$date": 1582267402315
      }
    }
    

# test = templateModelResponse()
# y =  test.modelAdapter(x)
# print(y)
print(type(x))

# y = map(test.test, x)

# z = test.test2(list(y))

# print(z)

# x = templateModelResponse()
# print(x.__dict__)