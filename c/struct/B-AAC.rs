
#[warn(dead_code)]
struct Person{
    name: String,
    age: u8,
}

impl Person {
    fn say_hi(&self){
        println!("Hi");
    }
}


fn main() {
    let nuni = Person {
        name: String::from("nuni"),
        age: 20,
    };

    nuni.say_hi();
}

