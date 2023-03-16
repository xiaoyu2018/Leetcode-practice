public class temp {

    public void foo1(String... strings) {
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
        System.out.println(111);
    }
}



interface Ishit {
    static String filed1 = "111";
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

    public Student(String id,int age,String name) {
        super(name, age);
        this.ID = id;
    }
    
    
}
