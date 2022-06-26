
import cProfile


cProfile.run("for i in range(1000000): i = i* i");
cProfile.runctx("for n in range(1000000): n*i*i*i*j*j", { 'i': 23 }, { 'j': 34})

print cProfile.label("for n in range(1000000): n*i*i*i*j*j")
