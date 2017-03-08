#!/usr/bin/env python

class Block:
    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.data = data
        self.previousHash = previousHash
        self.hash = hash
        self.timestamp = timestamp

    def __str__(self):
        return "Block number: " + `self.index` + " contains: " + self.data
