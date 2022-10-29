class MyLinkedList {
    
    public class Node{
        Node next;
        int value;
        public Node(int v){
            this.value = v;
        }
    }

    Node head  = null;
    Node tail  = null;
    int size = 0;
       
    public int get(int index) {
        int i = 0;
        Node current = this.head;
        while (current!=null){
            if(i == index){
                return current.value;
            }else{
                System.out.println(current.value);
                current = current.next;
                i+=1;
            }
        }
        return -1;
    }
    
    public void addAtHead(int val) {
        if(this.head != null){           
            Node h = this.head;
            this.head = new Node(val);
            this.head.next = h;
        }else{
            this.head = new Node(val);
            this.head.next = this.tail;
        }
        size+=1;
    }
    
    public void addAtTail(int val) {
        if(this.tail != null){            
            this.tail.next = new Node(val);
            this.tail = this.tail.next;
        }else{
            this.tail = new Node(val);
        }
        size+=1;
    }
    
    public void addAtIndex(int index, int val) {
        int i = 0;
        Node current = this.head;
        while (current!=null){
            if(i == index){
                Node next = current.next;
                current.next = new Node(val);
                current.next.next = next;
                break;
            }else{
                current = current.next;
                i+=1;
            }
        }
        size+=1;
    }
    
    public void deleteAtIndex(int index) {
        int i = 0;
        Node current = this.head;
        while (current!=null){
            if(i+1 == index){
                if(current.next!=null){                
                    current.next = current.next.next;
                }else{
                    current.next = null;
                }
                size-=1;
                break;
            }else{
                current = current.next;
                i+=1;
            }
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
