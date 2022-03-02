from monero.wallet import Wallet
from monero.backends.jsonrpc import JSONRPCWallet
from monero.exceptions import NotEnoughMoney

from decimal import Decimal
from time import sleep


def recursive_func(accs):
    while accs[0][0].balance(unlocked="true") <= 0.0:
        sleep(60)
        
    new_accs = []
    for i in range(0, len(accs)):
        for j in range(0, len(accs[i])):
            temp = []
            for k in range(0, 15):
                temp.append(w.new_account())
            new_accs.append(temp)

    new_accs_index = 0
    for i in range(0, len(accs)):
        for j in range(0, len(accs[i])):
            try:
                accs[i][j].transfer_multiple([(new_accs[new_accs_index][0].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][1].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][2].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][3].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][4].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][5].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][6].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][7].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][8].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][9].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][10].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][11].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][12].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][13].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001)),
                (new_accs[new_accs_index][14].address(), (accs[i][j].balance(unlocked="true")/15)-Decimal(0.0001))
                ], priority=3)
                new_accs_index+=1
            except NotEnoughMoney:
                print("not enough money")
                return False
            except Exception as e:
                print(e)
                return False  
    return recursive_func(new_accs)
