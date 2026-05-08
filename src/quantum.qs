namespace mkvqe{
import Std.Arrays.Partitioned;
import Std.Convert.IntAsDouble;
operation ansatz(qs:Qubit[],t:Double[]):Unit{
    Ry(t[0],qs[0]);
    Ry(t[1],qs[1]);
    Ry(t[2],qs[2]);
    Ry(t[3],qs[3]);
    CNOT(qs[0],qs[1]);
    CNOT(qs[1],qs[2]);
    CNOT(qs[2],qs[3]);
    Ry(t[4],qs[0]);
    Ry(t[5],qs[1]);
    Ry(t[6],qs[2]);
    Ry(t[7],qs[3]);
}
operation rotatebasis(q:Qubit,gate:String):Unit{
    if(gate=="Z"or gate=="I"){
        I(q);
    }
    elif(gate=="X"){
        H(q);
    }
    elif(gate=="Y"){
        Adjoint S(q);
        H(q);
    }
    
}
operation expval(gates:String[],qubits:Int[],t:Double[],shots:Int):Double{
    mutable parity=0;
    for i in 1..shots{
        mutable ones=0;
        use qs=Qubit[4];
        ansatz(qs,t);
        for i in 0..Length(qubits)-1{
            rotatebasis(qs[qubits[i]],gates[i]);
        }
        let r=M(qs[0]);
        let q=M(qs[1]);
        let s=M(qs[2]);
        let p=M(qs[3]);
        if(r==One){
            set ones+=1;
        }
        if(q==One){
            set ones+=1;
        }
        if(s==One){
            set ones+=1;
        }
        if(p==One){
            set ones+=1;
        }
        if(ones%2==0){
            set parity+=1;
        }
        else{
            set parity-=1;
        }
        ResetAll(qs);
        
    }
    return IntAsDouble(parity)/IntAsDouble(shots);
}
}

