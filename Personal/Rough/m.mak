#Makefile contents here

PROGRAM := we7_solution
SRCS := $(wildcard *.cpp)
OBJS := ${SRCS:.cpp=.o}
CFLAGS := -g -Wall -std=c++11
CC = g++

$(PROGRAM): $(SRCS)
	@$(CC) $(SRCS) -o $(PROGRAM) $(CFLAGS)

clean:
	@rm -f gdb ./$(PROGRAM)