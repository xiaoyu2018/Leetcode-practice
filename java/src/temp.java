public class temp {

    public void foo1(String... strings) {
        Person p = new Person(null, 0);
        Student s = new Student(null, 0, null);
        Person pp = s;

        Student ss = pp instanceof Student ? (Student) pp : null;
        Student.foo();

    }
}

interface Ishit {
    static String filed1 = "111";
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
