import Std.Convert.IntAsDouble;
open Microsoft.Quantum.Math;
operation ansatz(qs:Qubit[],t1:Double , t2: Double , t3:Double , t4:Double):Unit{
    Ry(t1,qs[0]);
    Ry(t2,qs[1]);
    CNOT(qs[0],qs[1]);
    Ry(t3,qs[0]);
    Ry(t4,qs[1]);
}
// IZ EXPECTATION
operation expIz(t1:Double,t2:Double,t3:Double,t4:Double,shots:Int): Double{
    mutable zeros=0;
    mutable ones=0;
    for i in 1..shots{
        use qs=Qubit[2];
        ansatz(qs,t1,t2,t3,t4);
        let r=M(qs[0]);
        if r==Zero{
            set zeros+=1;
        }
        else{
            set ones+=1;
        }
        ResetAll(qs);    
    }
    return IntAsDouble(zeros-ones)/IntAsDouble(shots);//<z0>=(n0-n1)/(n0+n1)
}
//ZZ EXPECTATION
operation expzz(t1:Double,t2:Double,t3:Double,t4:Double,shots:Int): Double{
    mutable same=0;
    mutable diff=0;
    for i in 1..shots{
        use qs=Qubit[2];
        ansatz(qs,t1,t2,t3,t4);
        let r=M(qs[0]);
        let s=M(qs[1]);
        if r==s{
            set same+=1;
        }
        else{
            set diff+=1;
        }
        ResetAll(qs);    
    }
    return IntAsDouble(same-diff)/IntAsDouble(shots);//<zz>=(nsame-diff)/(nsame0+ndiff)
}
//XX EXPECTATION
operation expxx(t1:Double,t2:Double,t3:Double,t4:Double,shots:Int): Double{
    mutable same=0;
    mutable diff=0;
    for i in 1..shots{
        use qs=Qubit[2];
        ansatz(qs,t1,t2,t3,t4);
        H(qs[0]);
        H(qs[1]);
        let r=M(qs[0]);
        let s=M(qs[1]);
        if r==s{
            set same+=1;
        }
        else{
            set diff+=1;
        }
        ResetAll(qs);    
    }
    return IntAsDouble(same-diff)/IntAsDouble(shots);//<zz>=(nsame-diff)/(nsame0+ndiff)
}
//YY EXPECTATION
operation expyy(t1:Double,t2:Double,t3:Double,t4:Double,shots:Int): Double{
    mutable same=0;
    mutable diff=0;
    for i in 1..shots{
        use qs=Qubit[2];
        ansatz(qs,t1,t2,t3,t4);
        Adjoint S(qs[0]);
        Adjoint S(qs[1]);
        H(qs[0]);
        H(qs[1]);
        let r=M(qs[0]);
        let s=M(qs[1]);
        if r==s{
            set same+=1;
        }
        else{
            set diff+=1;
        }
        ResetAll(qs);    
    }
    return IntAsDouble(same-diff)/IntAsDouble(shots);//<zz>=(nsame-diff)/(nsame0+ndiff)
}
//ZI EXPECTATION
operation expzI(t1:Double,t2:Double,t3:Double,t4:Double,shots:Int): Double{
    mutable zeros=0;
    mutable ones=0;
    for i in 1..shots{
        use qs=Qubit[2];
        ansatz(qs,t1,t2,t3,t4);
        let r=M(qs[1]);
        if r==Zero{
            set zeros+=1;
        }
        else{
            set ones+=1;
        }
        ResetAll(qs);    
    }
    return IntAsDouble(zeros-ones)/IntAsDouble(shots);//<z0>=(n0-n1)/(n0+n1)
}
operation Main(): Unit{
    
}