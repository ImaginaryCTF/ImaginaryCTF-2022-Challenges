# CyberCook
**Category:** Web
**Difficulty:** Medium-Hard
**Author:** Eth007

## Description

I've been working on a new and improved version of CyberChef. It's still under construction and only supports one function right now, but I can assure you that it's blazing fast!

## Distribution

- Website link

## Deploy notes

- docker-compose, might need privileged

## Solution

There's a heap overflow in the WASM code for base64, as it assumes that the base64 encoded text is the same length as the unencoded text. We can therefore write base64 encoded data to the next chunk, which happens to hold the pointer that will be returned to us. We can use the second vulnerability, that the base64 alphabet is missing one character, to write a null byte as part of the address (actually not sure if this is neccesary), and we can change the pointer to point at our original input. I put a short XSS payload that eval()s q.a, which will eval() the GET parameter `a`. This works because the loader code loads all the GET parameters into `q`.
