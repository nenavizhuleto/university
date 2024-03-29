build: $(wildcard *.c)
	find -type f -name '*.c' | xargs -I% cc % -o bin/$$(echo "%" | cut -d "." -f 1) -lm
