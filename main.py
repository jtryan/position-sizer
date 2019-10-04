#!/usr/local/bin/python3
import argparse


# function to print the fraction of
# a given rational number
def reducedfraction(d):
    # function that converts a rational number
    # to the reduced fraction
    b = d.as_integer_ratio()

    # reduced the list that contains the fraction
    return b


# driver code
b = reducedfraction(2.5)
print
b[0], "/", b[1]


def main():
    # parse command line
    parser = argparse.ArgumentParser(description='Calculate trade position size')
    parser.add_argument('--balance', type=float, required=True, help='Account balance')
    parser.add_argument('--bid', type=float, required=True, help='Stock Bid Price')
    parser.add_argument('--risk', type=float, default=0.01, help='Trade Risk % in decimal')
    parser.add_argument('--target', type=float, default=0.15, help='Profit Target % in decimal')
    parser.add_argument('--loss', type=float,  default=0.05, help='Trade Loss in decimal')
    args = parser.parse_args()

    balance = args.balance
    bid = args.bid
    risk = args.risk
    target = args.target
    loss = args.loss

    money_at_risk = balance * risk
    cents_at_risk = bid - (bid*(1-loss))
    position_size = money_at_risk / cents_at_risk
    print('Win/Loss ratio is: ' + str(round(target/loss)), '/ 1')
    print('Your position size is: ' + str(round(position_size)))
    print('Set your stop loss at: ' + str(round(bid*(1-loss))))
    print('Take profit at: ' + str(round(bid*(1+target))))


if __name__ == '__main__':
    main()
