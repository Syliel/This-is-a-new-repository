#!/usr/bin/env python3
import ky

def main():
    storage = ky.KV("https://api.sethdmoore.com/kv/")
    storage.test()
    store.create("this_is_the_key",["these", "are", "the", "values"])

if __name__ == '__main__':
    main()
