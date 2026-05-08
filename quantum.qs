import Std.Convert.IntAsDouble;
open Microsoft.Quantum.Math;
operation ansatz(qs:Qubit[],t1:Double , t2: Double , t3:Double , t4:Double):Unit{
    Ry(t1,qs[0]);
    Ry(t2,qs[1]);
    CNOT(qs[0],qs[1]);
    Ry(t3,qs[0]);
    Ry(t4,qs[1]);
}

operation expz0(t1:Double,t2:Double,t3:Double,t4:Double,shots:Int): Double{
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
operation Main(): Double{
    let exp = expz0(
        PI()/4.0,
        PI()/3.0,
        PI()/2.0,
        PI()/2.0,
        100
    );
    return exp;
}