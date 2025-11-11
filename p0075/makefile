CXX=g++
LDFLAGS=-O3

all: brut imp

brut: p75Brut.cc
	$(CXX) -o $@ $^ $(LDFLAGS)

imp: p75Brutimp3.cc
	$(CXX) -o $@ $^ $(LDFLAGS)


clean:
	rm -rf brut imp
