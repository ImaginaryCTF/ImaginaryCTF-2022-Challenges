vuln: vuln.c
	gcc vuln.c -o vuln -no-pie -Wl,-z,relro,-z,now
	pwninit
	mv vuln_patched vuln

clean:
	rm -rf vuln
