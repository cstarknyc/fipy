## -*-Pyth-*-
 # ########################################################################
 # FiPy - a finite volume PDE solver in Python
 # 
 # FILE: "iterator.py"
 #                                     created: 10/31/06 {9:50:24 AM}
 #                                 last update: 10/31/06 {1:32:39 PM}
 # Author: Jonathan Guyer <guyer@nist.gov>
 # Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 # Author: James Warren   <jwarren@nist.gov>
 #   mail: NIST
 #    www: <http://www.ctcms.nist.gov/fipy/>
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are 
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 # 
 # History
 # 
 # modified   by  rev reason
 # ---------- --- --- -----------
 # 2006-10-31 JEG 1.0 original
 # 
 # ########################################################################
 ##

__docformat__ = 'restructuredtext'

class Iterator:
    def __init__(self, iterates=()):
        self.iterates = iterates
        
    def sweepFn(iterates, dt):
        residual = 0
        for var, eqn, bcs in iterates:
            residual = max(residual, eqn.sweep(var=var, dt=dt, boundaryConditions=bcs))
             
        return residual
    sweepFn = staticmethod(sweepFn)
         
    def successFn(iterates, dt, dtTry, elapsed, *args, **kwargs):
        pass
    successFn = staticmethod(successFn)
         
    def failFn(iterates, dtTry, *args, **kwargs):
        pass
    failFn = staticmethod(failFn)

    def _step(self, dt, elapsed, sweepFn, failFn, *args, **kwargs):
        sweepFn(iterates=self.iterates, dt=dt, *args, **kwargs) 
        return dt, dt
         
    def step(self, dt, maxError=1e-3, sweepFn=None, successFn=None, failFn=None, *args, **kwargs):
        sweepFn = sweepFn or self.sweepFn
        successFn = successFn or self.successFn
        failFn = failFn or self.failFn
     
        dtTry = dt
        elapsed = 0.
         
        while elapsed < dt:
             
            for var, eqn, bcs in self.iterates:
                var.updateOld()
                 
            dtDid, dtTry = self._step(dt=dtTry, elapsed=elapsed, maxError=maxError, 
                                      sweepFn=sweepFn, failFn=failFn,
                                      *args, **kwargs)
            elapsed += dtDid
                                
            successFn(iterates=self.iterates, 
                      dtTry=dtTry, elapsed=elapsed, dt=dt, *args, **kwargs)

            dtTry = min(dtTry, dt - elapsed)

