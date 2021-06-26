//
// Created by paulyhedral on 6/25/21.
//

import Vapor
import Fluent


public final class VolumeAuthorPivot : Model {
    static let schema = "volume_authors"

    @ID
    var id : UUID?

    @Parent(key: "volumeId")
    var volume : Volume

    @Parent(key: "authorId")
    var author : Author

    init() {}

    init(id : UUID? = nil, volume : Volume, author : Author) throws {
        self.id = id
        self.$volume.id = try volume.requireID()
        self.$author.id = try author.requireID()
    }

}
