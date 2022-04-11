

CFLAGS = $(pkg-config --cflags  python-3.10)
LIBS =$(pkg-config --libs  python-3.10)
LIBS += -lpython3.10



all: high_level
	gcc  $(CFLAGS) $(LIBS)   -lpython3.10  high_level.c -o high_level

