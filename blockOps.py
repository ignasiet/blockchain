#!/usr/bin/env python
import hashlib
import BaseHTTPServer
from block import Block
from datetime import datetime
from miniserver import MyMiniServer


def getBlocks(s):
    if not s.blockchain:
        s.addBlock(getGenesisBlock())
    retStr = []
    for b in s.blockchain :
        print b
        retStr.append(b)
    return retStr


def calculateHash(index, previousHash, timestamp, data):
    m = hashlib.sha256()
    m.update(`index` + previousHash + `timestamp` + data)
    return m.digest

def calculateHashForBlock(block):
    return calculateHash(block.index, block.previousHash, block.timestamp, block.data)

def generateNextBlock(server, blockData):
    #previousBlock = getLatestBlock()
    if not server.blockchain:
        server.addBlock(getGenesisBlock())
    previousBlock = server.blockchain[-1]
    nextIndex = previousBlock.index + 1
    nextTimestamp = datetime.now()
    nextHash = calculateHash(nextIndex, previousBlock.hash, nextTimestamp, blockData);
    return Block(nextIndex, previousBlock.hash, nextTimestamp, blockData, nextHash);

def getGenesisBlock():
    return Block(0, "0", 1465154705, "First Genesis Block", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7")

def verifyValidityNewBlock(newBlock, previousBlock):
    if previousBlock.index + 1 != newBlock.index:
        print 'Invalid index'
        return false
    elif previousBlock.hash != newBlock.previousHash:
        print 'Invalid Previous Hash'
        return false
    elif calculateHashForBlock(newBlock) != newBlock.hash:
        print 'Invalid hash: ' + calculateHashForBlock(newBlock) + ' ' + newBlock.hash
        return false
    return true


def replaceChain(newBlocks):
    if isValidChain(newBlocks) and newBlocks.length > blockchain.length:
        print 'Received blockchain is valid. Replacing current blockchain with received blockchain'
        blockchain = newBlocks;
        #broadcast(responseLatestMsg());
    else:
        print 'Received blockchain invalid'


def isValidChain (blockchainToValidate):
    if blockchainToValidate[0].hash != getGenesisBlock().hash:
        return false
    tempBlocks = [blockchainToValidate[0]];
    for i in xrange(1,len(blockchainToValidate)):
        if verifyValidityNewBlock(blockchainToValidate[i], tempBlocks[i - 1]):
            tempBlocks.append(blockchainToValidate[i]);
        else:
            return false
    return true
