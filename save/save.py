import json

def save_game(saveName, totalAmount, upgradeCosts, earnPerClick):
    with open('./save/save_file.json', 'r') as save_file:
        old_data = json.load(save_file)

    data = {
        "saveName": saveName,
        "totalAmount": totalAmount,
        "upgradeCosts": upgradeCosts,
        "earnPerClick": earnPerClick
    }
    
    feedback = 200

    try:
        for saves in old_data:
            print(saves)
            if saveName == saves["saveName"]:
                data = None
                feedback = 409
            break
    except:
        pass

    old_data.append(data)

    new_data = json.dumps(old_data, indent=4)

    if data is not None:
        with open('./save/save_file.json', 'w') as save_file:
            save_file.write(new_data)

    return feedback

def load_game(saveName):
    with open('./save/save_file.json', 'r') as save_file:
        data_file = json.load(save_file)
    
        for saveName in data_file["saveName"]:
            if saveName == data_file["saveName"]:

                totalAmount = data_file["totalAmount"]
                upgradeCosts = data_file["upgradeCosts"]
                earnPerClick = data_file["earnPerClick"]

                feedback = 200

                return saveName, totalAmount, upgradeCosts, earnPerClick, feedback
            break

save_game("new", 1,{'a': 3, 'b': 3}, 2)