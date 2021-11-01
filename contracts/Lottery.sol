// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    constructor(address _priceFeedAmount) public {
        usdEntryFee = 50 * 10**18;
    }

    function enter() public {
        // minimum: $50
        players.push(msg.sender);
    }

    function getEntranceFee() public {}

    function startLottery() public {}

    function endLottery() public {}
}
