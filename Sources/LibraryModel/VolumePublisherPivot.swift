//
// Created by paulyhedral on 6/25/21.
//

import Vapor
import Fluent


public final class VolumePublisherPivot : Model {
    static let schema = "volume_publishers"

    @ID
    var id : UUID?

    @Parent(key: "volumeId")
    var volume : Volume

    @Parent(key: "publisherId")
    var publisher : Publisher

    init() {}

    init(id : UUID? = nil, volume : Volume, publisher : Publisher) throws {
        self.id = id
        self.$volume.id = try volume.requireID()
        self.$publisher.id = try publisher.requireID()
    }

}
