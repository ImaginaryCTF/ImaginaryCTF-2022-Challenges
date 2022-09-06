vuln: vuln.c
	gcc vuln.c -o vuln -lseccomp -no-pie -Wl,-z,relro,-z,now

clean:
	rm -rf vuln
