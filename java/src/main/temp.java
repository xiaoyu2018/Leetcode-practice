package main;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.time.LocalDate;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Stack;

public class temp {

    public void foo1(String... strings) throws Exception {
        // Person p = new Person(null, 0);
        // Student s = new Student(null, 0, null);
        // Person pp = s;

        // Student ss = pp instanceof Student ? (Student) pp : null;
        // Student.foo();
        // Outer o1 = new Outer("1");
        // System.out.println(o1.getField());
        // Outer.Inner o2 = o1.new Inner("2");
        // System.out.println(o2.field);
        // System.out.println(o1.getField());
        // Integer i1 = 2;
        // i1 = 3;
        // int x = -1;
        // assert x > 1;
        // System.out.println(111);

        // Ishit ds = new DogShit();
        // Class t1 = DogShit.class;
        // Method m1 = t1.getDeclaredMethod("emitSmell", null);
        // m1.invoke(ds, null);
        // Class t2 = t1.getInterfaces()[0];
        // System.out.println(t2.getName());
        
        // Student s = Student.class.getConstructor().newInstance();
        // s.study();
        // List<Integer> arr = new ArrayList<>();
        // List<Integer> l1 = new ArrayList<>();
        // List<Double> l2 = new ArrayList<>();
        // List<Object> l3 = new ArrayList<>();
        // List<? extends Number> l4 = l1;
        // l4.get(0);

        // List<? super String> l5 = l3;
        // l5.set(0, "ad");
        
        // l1.add(Integer.valueOf(213));
        // LocalDate d = LocalDate.now();
        // d.getYear();
        // System.out.println(d);

        List<Integer> l1 = List.of(1, 2, 33);
        List<String> l2 = new ArrayList<>();
        for(int i=0;i<10;i++)
        {
            // l1.add(i);
            l2.add(String.valueOf(i));
        }

        Map<Student, Integer> memo = new HashMap<>();
        Student s1 = new Student("002", 22, "Tim");
        memo.put(new Student("001", 22, "Tom"), 565);
        memo.put(new Student("002", 22, "Tim"), 575);
        System.out.println(memo.get(s1));
        
        
    }
}



interface Ishit {
    static String filed1 = "111";

    void emitSmell();
}
class DogShit implements Ishit
{

    @Override
    public void emitSmell() {
        System.out.println("dogshit smell is emitting");
    }
    
}

class Outer
{
    private String field;

    public Outer(String string) {
        field = string;
    }

    public String getField()
    {
        return field;
    }
    
    class Inner
    {
        public String field;
        
        public Inner(String field) {
            Outer.this.field = "decrepted";
            this.field=field;
        }    
    }
}

class Person 
{
    protected String name;
    protected int age;

    static void foo() {
        
    }
    public Person(String name,int age) {
        this.age=age;
        this.name=name;
    }
}

class Student extends Person 
{
    private String ID;
    public Student() {
        super("Tom", 11);
        this.ID = "000";
    }
    public Student(String id,int age,String name) {
        super(name, age);
        this.ID = id;
    }
    
    public void study()
    {
        System.out.println(name + "is studying...");
    }
    
    @Override
    public int hashCode()
    {
        return Objects.hash(ID, name, age);
    }

    @Override
    public boolean equals(Object o)
    {
        if(o instanceof Student)
        {
            Student s = (Student) o;
            return s.name.equals(this.name)&&
                    s.age == this.age&&
                    s.ID.equals(this.ID);
        }
        return false;
    }
    
}
