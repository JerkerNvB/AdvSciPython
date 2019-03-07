from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("This is rank %d" %rank)

#initializing variables. mpi4py requires that we pass numpy objects.
integral = numpy.zeros(1)
total = numpy.zeros(1)


integral += rank

comm.Barrier()

comm.Allreduce(integral, total)
print ("the total: " + str(total))

total -= total

comm.Reduce(integral, total, op=MPI.SUM, root=0)
print ("the total for rank " + str(rank) + " : " + str(total))
