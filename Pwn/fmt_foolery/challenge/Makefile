fmt_fun: fmt_foolery.c
	gcc fmt_foolery.c -o fmt_foolery -no-pie -L -z,relro -Wl,-z,relro,-z,now -lseccomp

clean:
	rm -rf fmt_foolery

